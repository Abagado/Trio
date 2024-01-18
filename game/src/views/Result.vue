<script lang="ts">
import axios from 'axios';
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  data() {
    return {
      users: []
    };
  },
  created() {
    this.fetchUsers();
  },
  methods: {
    fetchUsers() {
      axios.get('http://127.0.0.1:8080/user/users/?format=json')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error('Ошибка получения данных:', error);
        });
    },
    end() {
      this.$router.push({ name: 'Home' });
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
