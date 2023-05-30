<template>
    <div class="main">

        <div class="tarefas">
            <div v-for="tarefa in tarefas" :key="tarefa.id">
                {{ tarefa.nome }}
            </div>
        </div>

    </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import todoApi from '../api/todo'

const todo_api = new todoApi();
const tarefas = ref([])

onMounted(
    async function buscarTarefas() {
        tarefas.value = await todo_api.buscarTarefas();
    }
)
</script>

<style scoped>

.tarefas {
    display: flex;
    flex-direction: column;
    border: 1px solid white;
    padding: 1vh;
    text-align: center;
}

</style>