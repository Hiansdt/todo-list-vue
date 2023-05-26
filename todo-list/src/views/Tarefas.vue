<template>
    <div class="main">
        <div v-for="tarefa in tarefas" :key="tarefa.id">
            {{ tarefa.nome }}
        </div>
    </div>
</template>

<script setup>

import { ref } from 'vue'
import lojaApi from '../api/todo.js'
import axios from "axios"

const loja_api = new lojaApi();
const tarefas = ref([])

async function buscarTarefas() {
    tarefas.value = await loja_api.buscarTarefas();
}

buscarTarefas();

</script>