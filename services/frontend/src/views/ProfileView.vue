<template>
    <section class="max-w-4xl mx-auto mt-8">
      <h1 class="text-2xl font-bold mb-4">Your Profile</h1>
      <hr class="mb-4"/>
      <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <p class="mb-4"><strong>Full Name:</strong> <span>{{ user.full_name }}</span></p>
        <p class="mb-4"><strong>Username:</strong> <span>{{ user.username }}</span></p>
        <p>
          <button @click="deleteAccount()" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
            Delete Account
          </button>
        </p>
      </div>
    </section>
  </template>
    
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Profile',
    created() {
      this.$store.dispatch('viewMe');
    },
    computed: {
      ...mapGetters({ user: 'stateUser' }),
    },
    methods: {
      ...mapActions(['deleteUser']),
      async deleteAccount() {
        try {
          await this.deleteUser(this.user.id);
          await this.$store.dispatch('logOut');
          this.$router.push('/');
        } catch (error) {
          console.error(error);
        }
      },
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  