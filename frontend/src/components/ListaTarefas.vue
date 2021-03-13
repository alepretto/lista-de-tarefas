<template>
  <div id="lista-tarefas">
    <div class="tarefa" v-for="tarefa in tarefas" :key="tarefa.id_tarefa">
      <div class="superior">
        <span>{{ tarefa.nome }}</span>
        <span>{{ tarefa.dataCriacao }}</span>
      </div>
      <div class="inferior">
        <span>{{ tarefa.descricao }}</span>
        <span>Concluido: {{ tarefa.concluido }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListaTarefas",
  data: function() {
    return {
      tarefas: [
        {
          id_tarefa: 1,
          nome: "Terminar API da lista de tarefas",
          dataCriacao: "06/03/2021",
          descricao:
            "Terminar de construir o backend da aplicação de lista de tarefas",
          concluido: false
        },
        {
          id_tarefa: 2,
          nome: "Terminar API da lista de tarefas",
          dataCriacao: "06/03/2021",
          descricao:
            "Terminar de construir o backend da aplicação de lista de tarefas",
          concluido: false
        },
        {
          id_tarefa: 3,
          nome: "Terminar API da lista de tarefas",
          dataCriacao: "06/03/2021",
          descricao:
            "Terminar de construir o backend da aplicação de lista de tarefas",
          concluido: false
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.tarefa {
  border: 1px solid black;
  border-radius: 8px;

  background-color: #e0d9d9;
  opacity: 70%;
  color: rgb(0, 0, 0);

  max-width: 820px;
  margin: 12px auto;

  padding: 8px;
  .superior,
  .inferior {
    margin: 6px;
    span {
      display: block;
    }
    display: flex;
    justify-content: space-between;
  }

  .superior {
    margin-bottom: 20px;
  }

  .inferior {
    margin-top: 20px;
  }
}
</style>
