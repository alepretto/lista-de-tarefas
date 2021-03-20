<template>
  <div id="tarefa">
    <div class="primeiro">
      <h1>{{ tarefa.nome }}</h1>
      <span>{{ tarefa.descricao }}</span>
    </div>
    <div class="meio">
      <h5>Aberta: {{ tarefa.created_at | dateFormat }}</h5>
      <span :style="{ color: statusTarefa.cor }">{{ statusTarefa.msg }}</span>
    </div>
    <div class="ultimo">
      <button class="btn-ok" @click="finalizaTarefa">
        OK
      </button>
      <button class="btn-open" @click="abrirTarefa">-</button>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "Tarefa",

  props: ["tarefa"],

  methods: {
    finalizaTarefa() {
      this.$http
        .patch(`/tarefas/${this.tarefa.id_tarefa}/concluir`)
        .then(() => (this.tarefa.concluido = true));
    },
    abrirTarefa() {
      this.$http
        .patch(`/tarefas/${this.tarefa.id_tarefa}/abrir`)
        .then(() => (this.tarefa.concluido = false));
    },
  },
  computed: {
    statusTarefa() {
      if (this.tarefa.concluido == false) {
        return { msg: "Em Aberto", cor: "#EB2323" };
      } else {
        return { msg: "Concluido", cor: "#25DD43" };
      }
    },
  },

  filters: {
    dateFormat(string_date) {
      if (string_date) {
        return moment(String(string_date)).format("MM/DD/YYYY HH:mm");
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/baseColors.scss";

#tarefa {
  border-radius: 8px;

  background-color: #38383a;
  color: #ffffff;

  max-width: 900px;
  margin: 23px auto;

  padding: 14px;

  display: flex;
  justify-content: space-between;

  .primeiro,
  .meio,
  .ultimo {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    span {
      display: block;
    }

    button {
      display: block;
      border-radius: 10px;
      border: none;

      margin-top: 1em;
      padding: 6px;

      width: 30px;
      height: 30px;

      font-size: 0.7em;
      color: snow;

      cursor: pointer;

      transition: 0.4s;
    }
    .btn-ok {
      background-color: $soft-green;
      &:hover {
        background-color: $strong-green;
      }
    }
    .btn-open {
      background-color: $strong-red;
      &:hover {
        background-color: $soft-red;
      }
    }
  }

  .primeiro {
    flex: 1;
  }

  .meio {
    font-weight: lighter;
    text-align: center;
    text-align: center;
    flex: 0.5;
    span {
      font-weight: bold;
    }
  }

  .ultimo {
    flex: 0.05;
  }
}
</style>
