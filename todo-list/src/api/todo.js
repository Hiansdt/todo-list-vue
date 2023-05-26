import axios from "axios";

export default class todoApi {
    async buscarTarefas() {
        const { data } = await axios.get("tarefas/");
        return data;    
    }
}