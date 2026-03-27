'use server';

import { prisma } from './db';
import fs from 'fs';
import path from 'path';

const BASE_DOCUMENTS_PATH = 'C:/Users/thiag/TM-MEUS-APPS/.NEXT APPS/AUTO RELATÓRIO/AutoRelatorioV1/DOCUMENTOS/ENTRADA';

export async function saveCapture(formData: FormData) {
  const orderId = formData.get('orderId') as string;
  const clientName = formData.get('clientName') as string;
  const areaValue = formData.get('area') as string; // ex: "- Área externa"
  const environmentValue = formData.get('environment') as string; // ex: "Jardim"
  const type = formData.get('type') as string; // VISTA_AMPLA, SERVICO, DETALHE
  const description = formData.get('description') as string;
  const file = formData.get('file') as File;

  if (!orderId || !areaValue || !environmentValue || !file) {
    throw new Error('Dados insuficientes para a captura');
  }

  // Define o nome da pasta do item baseado no tipo
  let itemFolderName = '';
  if (type === 'VISTA_AMPLA') {
    itemFolderName = '- Vista ampla';
  } else if (type === 'SERVICO') {
    // Busca o número sequencial atual para serviços nesta ordem/área/ambiente
    const count = await prisma.orderItem.count({
      where: { orderId, area: areaValue, environment: environmentValue, type: 'SERVICO' }
    });
    const seq = (count + 1).toString().padStart(2, '0');
    itemFolderName = `${seq}. ${description || 'Serviço sem nome'}`;
  } else {
    itemFolderName = `... Detalhes ${description ? '- ' + description : ''}`;
  }

  // Caminho da estrutura: OS_CLIENTE / AREA / AMBIENTE / ITEM
  const folderPath = path.join(
    BASE_DOCUMENTS_PATH,
    `${orderId}_${clientName.replace(/\s+/g, '_')}`,
    areaValue,
    environmentValue,
    itemFolderName
  );

  // Garante que as pastas existem
  if (!fs.existsSync(folderPath)) {
    fs.mkdirSync(folderPath, { recursive: true });
  }

  // Salva o arquivo fisicamente
  const bytes = await file.arrayBuffer();
  const buffer = Buffer.from(bytes);
  const fileName = `${Date.now()}_${file.name}`;
  const filePath = path.join(folderPath, fileName);
  fs.writeFileSync(filePath, buffer);

  // Registra no banco de dados
  const orderItem = await prisma.orderItem.create({
    data: {
      orderId,
      area: areaValue,
      environment: environmentValue,
      type,
      description,
      photoPath: filePath
    }
  });

  return { success: true, item: orderItem };
}

export async function addComment(orderId: string, author: string, text: string) {
  return await prisma.comment.create({
    data: { orderId, author, text }
  });
}
