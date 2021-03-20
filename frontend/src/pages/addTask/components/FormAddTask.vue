<template>
  <div id="form-add-task">
    <header class="header">
      <h1>Nova Tarefa</h1>
    </header>
    <section>
      <form action="">
        <label for="nome-tarefa">Nome da tarefa:</label>
        <input
          type="text"
          id="nome-tarefa"
          placeholder="Digite o nome da tarefa..."
          v-model="nomeTarefa"
        />

        <label for="descricao-tarefa">Descrição da tarefa: </label>
        <textarea
          id="descricao-tarefa"
          cols="30"
          rows="8"
          placeholder="Digite a descrição da tarefa..."
          v-model="descricaoTarefa"
        ></textarea>
      </form>
      <footer>
        <router-link to="/">
          <button class="btn-voltar">Voltar</button>
        </router-link>

        <button class="btn-add-task" @click="adicionarTarefa">
          Adicionar Tarefa
        </button>
      </footer>
    </section>
  </div>
</template>

<script>
export default {
  name: "FormAddTask",

  data() {
    return {
      nomeTarefa: "",
      descricaoTarefa: "",
    };
  },

  methods: {
    adicionarTarefa() {
      let corpoMensagem = {
        nome: this.nomeTarefa,
        descricao: this.descricaoTarefa,
      };

      this.$http.post("/tarefas", corpoMensagem).then((res) => {
        if (res.status == 200) {
          this.nomeTarefa = "";
          this.descricaoTarefa = "";
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/baseColors.scss";

.header {
  display: flex;
  justify-content: flex-start;

  background-color: rgb(34, 34, 34);
  padding: 2em 12px;

  max-width: 920px;
  h1 {
    color: #0cd095;
  }
}

section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  padding: 12px 0;

  form {
    padding: 12px;
    margin: 1em 0;

    input,
    textarea {
      display: block;
      padding: 8px 12px;
      border-radius: 12px;

      width: 40em;
      border: 1px solid black;
    }

    input {
      height: 3em;
    }
    label {
      font-size: 1.5em;
      display: block;
      margin-top: 1em;
      margin-bottom: 0.5em;

      &:not(:first-child) {
        margin-top: 2em;
      }
    }
  }

  footer {
    display: flex;
    justify-content: space-between;

    button {
      display: block;

      padding: 12px;
      margin: 12px;

      width: 15em;
      height: 3em;

      border: none;
      border-radius: 12px;

      color: snow;
      transition: 0.5s;

      &.btn-voltar {
        background-color: $strong-red;
        &:hover {
          background-color: $soft-red;
        }
      }
      &.btn-add-task {
        background-color: $soft-green;
      }
      &:hover {
        background-color: $strong-green;
      }
    }

    a {
      color: snow;
      text-decoration: none;
    }
  }
}
</style>
