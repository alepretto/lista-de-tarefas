<template>
  <div id="big-number">
    <div class="info">
      <span class="info-number">{{ tarefasConcluidas }}</span>
      <span class="info-texto concluidas">Tarefas Concluidas</span>
    </div>

    <div class="info">
      <span class="info-number">{{ tarefasEmAberto }}</span>
      <span class="info-texto em-aberto">Tarefas Em Aberto</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ["tarefasConcluidas", "tarefasEmAberto"]
};
</script>

<style lang="scss" scoped>
@import "../styles/baseColors.scss";

#big-number {
  display: flex;
  justify-content: space-evenly;

  background-color: rgb(34, 34, 34);
  padding: 2em 12px;

  .info {
    text-align: center;

    .info-number {
      font-size: 2em;
      font-weight: bold;
      margin: 2px;
      color: snow;
    }

    .info-texto {
      font-size: 1.2em;
      letter-spacing: 1px;
    }
    .concluidas {
      color: $strong-green;
    }
    .em-aberto {
      color: $strong-red;
    }

    span {
      display: block;
    }
  }
}
</style>
