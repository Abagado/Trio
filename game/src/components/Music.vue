<template>
  <div>
    <!-- ваше существующее содержимое компонента -->
    <audio ref="audioTag" src="../assets/hang-drum-sister-moon%20(1).mp3" loop autoplay style="display: none"></audio>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  created() {
    // Получаем доступ к элементу <audio> через ref
    const audio = this.$refs.audioTag as HTMLAudioElement;
    // Убеждаемся, что объект аудио существует
    if (audio) {
      // Включаем звук и включаем автовоспроизведение
      audio.play();
    }
  }
});
</script>
