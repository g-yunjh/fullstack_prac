<template>
    <div class="max-w-4xl mx-auto mt-8">
      <section class="mb-8">
        <h1 class="text-2xl font-bold mb-4">Add new post</h1>
        <hr class="mb-4"/>
    
        <form @submit.prevent="submit" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div class="mb-4">
            <label for="title" class="block text-gray-700 text-sm font-bold mb-2">Title:</label>
            <input type="text" name="title" v-model="form.title" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
          </div>
          <div class="mb-4">
            <label for="content" class="block text-gray-700 text-sm font-bold mb-2">Content:</label>
            <textarea
              name="content"
              v-model="form.content"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            ></textarea>
          </div>
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Submit</button>
        </form>
      </section>
    
      <section>
        <h1 class="text-2xl font-bold mb-4">Posts</h1>
        <hr class="mb-4"/>
    
        <div v-if="posts.length">
          <div v-for="post in posts" :key="post.id" class="mb-4">
            <div class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
              <ul>
                <li class="mb-2"><strong>Post Title:</strong> {{ post.title }}</li>
                <li class="mb-2"><strong>Author:</strong> {{ post.author.username }}</li>
                <li>
                  <router-link :to="{ name: 'Post', params: { id: post.id } }" class="text-blue-500 hover:underline">View</router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
    
        <div v-else>
          <p class="text-gray-500">Nothing to see. Check back later.</p>
        </div>
      </section>
    </div>
  </template>
    
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Dashboard',
    data() {
      return {
        form: {
          title: '',
          content: '',
        },
      };
    },
    created() {
      this.$store.dispatch('getPosts');
    },
    computed: {
      ...mapGetters({ posts: 'statePosts' }),
    },
    methods: {
      ...mapActions(['createPost']),
      async submit() {
        await this.createPost(this.form);
        // 포스트 생성 후 폼을 초기화합니다.
        this.form.title = '';
        this.form.content = '';
      },
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles for better UX can be added here */
  </style>
  