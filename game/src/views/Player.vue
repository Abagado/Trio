<template>
  <div class="app">
    <!-- <p>Правила просты! Нажимайте левой кнопкой мышки</p> -->
    <img alt="logo" src="../assets/trio-logo(3).png">
    <Board />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Board from './Board.vue';

export default defineComponent({
  name: 'App',
  components: {
    Board
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  user-select:none;
  -webkit-user-select: none;
  -khtml-user-select:none;
  -moz-user-select: none;
  -ms-uzer-select:none;

}

</style>
