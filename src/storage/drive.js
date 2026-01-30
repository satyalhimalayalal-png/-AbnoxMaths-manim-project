import { CONFIG } from '../config.js';
import { saveData, loadData } from './idb.js';
export const saveToDrive = async (data, token) => { await saveData('hero', data); if(!token) return; /* Drive API call */ };
export const loadFromDrive = async (token) => { const local = await loadData('hero'); if(local) return local; /* Drive API load */ };