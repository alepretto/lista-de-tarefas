<template>
  <div id="dashboard">
    <section class="content">
      <big-numbers-tasks
        :tarefasEmAberto="tarefasEmABerto"
        :tarefasConcluidas="tarefasConcluidas"
      />

      <lista-tarefas />
    </section>
  </div>
</template>

<script>
import listaTarefas from "../components/ListaTarefas.vue";
import bigNumbersTasks from "../components/BigNumbersTask.vue";

export default {
  components: { listaTarefas, bigNumbersTasks },

  data: function() {
    return {
      tarefasEmABerto: 10,
      tarefasConcluidas: 3
    };
  }
};
</script>

<style>
.content {
  max-width: 920px;
  margin: 8em auto;
}
</style>
