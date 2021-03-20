<template>
  <div id="lista-tarefas">
    <div v-for="tarefa in tarefas" :key="tarefa.id_tarefa">
      <Tarefa :tarefa="tarefa" />
    </div>
  </div>
</template>

<script>
import Tarefa from "./Tarefa.vue";

export default {
  name: "ListaTarefas",
  props: ["tarefas"],
  components: { Tarefa },
};
</script>

<style lang="scss" scoped></style>
