<template>
  <div id="dashboard">
    <section class="content">
      <Big-numbers-tasks
        :tarefasEmAberto="tarefasEmABerto"
        :tarefasConcluidas="tarefasConcluidas"
      />
      <Dash-options v-bind:filtroTarefas.sync="filtroTarefas" />
      <Lista-tarefas class="caixa" :tarefas="listaTarefasFiltradas" />
    </section>
  </div>
</template>

<script>
import ListaTarefas from "./components/ListaTarefas.vue";
import BigNumbersTasks from "./components/BigNumbersTask.vue";
import DashOptions from "./components/DashOptions.vue";

export default {
  name: "Dashboard",
  components: { ListaTarefas, BigNumbersTasks, DashOptions },

  data: function() {
    return {
      tarefas: [],
      filtroTarefas: "todas",
    };
  },

  computed: {
    tarefasEmABerto() {
      return this.tarefas.filter((tarefa) => tarefa.concluido == false).length;
    },
    tarefasConcluidas() {
      return this.tarefas.filter((tarefa) => tarefa.concluido == true).length;
    },

    listaTarefasFiltradas() {
      if (this.filtroTarefas == "concluidas") {
        return this.tarefas.filter((tarefa) => tarefa.concluido == true);
      }
      if (this.filtroTarefas == "em-aberto") {
        return this.tarefas.filter((tarefa) => tarefa.concluido == false);
      }
      return this.tarefas;
    },
  },

  mounted() {
    this.$http("/tarefas").then((response) => {
      this.tarefas = response.data;
    });
  },
};
</script>

<style>
.content {
  max-width: 920px;
  margin: 4em auto;
}
</style>
