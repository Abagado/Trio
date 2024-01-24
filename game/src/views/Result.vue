<script lang="ts">
import axios from 'axios';
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';

interface User {
  id: number;
  username: string;
  score: number;
}

export default defineComponent({
  data() {
    return {
      users: [] as User[]
    };
  },
  created() {
    this.fetchUsers(); // Вызов метода в хуке created чтобы получить пользователей после создания компонента
  },
  methods: {
    fetchUsers() {
      axios.get('http://127.0.0.1:8080/user/users/')
          .then(response => {
            this.users = response.data; // Обновление данных пользователей
          })
          .catch(error => {
            console.error('Ошибка получения данных:', error); // Логирование ошибки
          });
    },
    end() {
      this.$router.push({ name: 'Home' }); // Перенаправление на домашнюю страницу
    }
  }
});
</script>


<template>
  <div>
    <h1>Таблица рейтинга</h1>
    <table>
      <thead>
        <tr>
          <th>Имя</th>
          <th>Баллы</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.username }}</td>
          <td>{{ user.score }}</td>
        </tr>
      </tbody>
    </table>
    <input type="submit" class="fadeIn fourth" @click="end" value="Назад">
  </div>
</template>
<style scoped>

</style>
