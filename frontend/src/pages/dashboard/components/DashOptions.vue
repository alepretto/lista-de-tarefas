<template>
  <div id="dash-options">
    <div class="primeira">
      <div class="caixa-filtro">
        <label for="todas">Todas</label>
        <input
          type="radio"
          id="todas"
          value="todas"
          v-model="filtroTarefas"
          @input="disparaFiltro"
        />
      </div>

      <div class="caixa-filtro">
        <label for="concluidas"> Concluidas</label>
        <input
          type="radio"
          id="concluidas"
          value="concluidas"
          @input="disparaFiltro"
          v-model="filtroTarefas"
        />
      </div>

      <div class="caixa-filtro">
        <label for="em-aberto">Em aberto</label>
        <input
          type="radio"
          id="em-aberto"
          value="em-aberto"
          @input="disparaFiltro"
          v-model="filtroTarefas"
        />
      </div>
    </div>

    <div class="segunda">
      <router-link to="/addTask">
        <button class="btn-page-addTask">+</button>
      </router-link>

      <button class="btn-page-estat">E</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "dashOptions",
  props: ["filtroTarefas"],

  methods: {
    disparaFiltro(event) {
      this.$emit("update:filtroTarefas", event.target.value);
    },
  },
};
</script>

<style lang="scss" scoped>
#dash-options {
  display: flex;
  justify-content: space-between;

  max-width: 57em;

  margin: 1em auto;

  .primeira {
    flex: 2;
    display: flex;
    justify-content: space-between;
    align-items: center;

    max-width: 40%;

    .caixa-filtro {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-around;

      width: 5em;

      input {
        display: block;
      }
    }
  }
  .segunda {
    display: flex;
    justify-content: flex-end;
    flex: 0.5;
  }

  button {
    display: block;
    border-radius: 10px;
    border: none;

    margin-left: 1em;
    width: 40px;
    height: 40px;
    padding: 7px;

    font-size: 1.3em;
    color: snow;
    font-weight: bold;
    cursor: pointer;
    transition: 0.4s;
  }
  a {
    text-decoration: none;
    color: snow;
  }

  .btn-page-addTask {
    background-color: #0cd095;
    &:hover {
      background-color: #31b562;
    }
  }

  .btn-page-estat {
    background-color: #28b7e4;
    &:hover {
      background-color: #0c84a9;
    }
  }
}
</style>
