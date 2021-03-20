<template>
  <div id="add-task">
    <form-add-task />
  </div>
</template>

<script>
import FormAddTask from "./components/FormAddTask.vue";

export default {
  components: { FormAddTask },
};
</script>

<style>
#add-task {
  max-width: 920px;
  margin: 4em auto;
}
</style>
