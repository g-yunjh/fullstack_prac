<template>
  <nav class="bg-white p-4 flex justify-between items-center">
    <div class="flex items-center">
      <img src="../assets/logo2.png" alt="Logo" class="h-12 w-12 mr-3"/>
      <h1 class="text-lg font-bold">성균관대</h1>
    </div>
    <div class="flex space-x-4">
      <router-link to="/login">
        <svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#5f6368"><path d="M784-120 532-372q-30 24-69 38t-83 14q-109 0-184.5-75.5T120-580q0-109 75.5-184.5T380-840q109 0 184.5 75.5T640-580q0 44-14 83t-38 69l252 252-56 56ZM380-400q75 0 127.5-52.5T560-580q0-75-52.5-127.5T380-760q-75 0-127.5 52.5T200-580q0 75 52.5 127.5T380-400Z"/></svg>
      </router-link>
      <router-link to="/profile">
        <svg xmlns="http://www.w3.org/2000/svg" height="30px" viewBox="0 -960 960 960" width="30px" fill="#5f6368"><path d="M234-276q51-39 114-61.5T480-360q69 0 132 22.5T726-276q35-41 54.5-93T800-480q0-133-93.5-226.5T480-800q-133 0-226.5 93.5T160-480q0 59 19.5 111t54.5 93Zm246-164q-59 0-99.5-40.5T340-580q0-59 40.5-99.5T480-720q59 0 99.5 40.5T620-580q0 59-40.5 99.5T480-440Zm0 360q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q53 0 100-15.5t86-44.5q-39-29-86-44.5T480-280q-53 0-100 15.5T294-220q39 29 86 44.5T480-160Zm0-360q26 0 43-17t17-43q0-26-17-43t-43-17q-26 0-43 17t-17 43q0 26 17 43t43 17Zm0-60Zm0 360Z"/></svg>
      </router-link>
    </div>
  </nav>

  <div class="flex flex-col items-center">
    <img src="../assets/ad.jpg" alt="Banner" class="min-w-[450px] max-w-lg max-h-[100px] object-cover rounded-lg"/>
  </div>

  <div class=" mx-auto bg-gray-100 flex flex-col items-center">
    <h1 class=" p-3 text-lg font-bold self-start">즐겨찾는 게시판</h1>
    <section class="min-w-[450px] bg-white rounded-lg mb-4">
      <div class="p-4">
        <ul>
          <li class="mb-3 flex items-center">
            <router-link to="/board/1" class="text-dark-500 font-bold hover:underline mr-2">인사캠 자유게시판</router-link>
            <p>콰이어트 플레이스 첫째날</p>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/2" class="text-dark-500 font-bold hover:underline mr-2">자과캠 자유게시판</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">인사캠 장터게시판</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">자과캠 장터게시판</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">정보게시판</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">취업진로</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">홍보게시판</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">동아리학회</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">성균맛집</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">교직이수자 모임</router-link>
          </li>
          <li class="mb-3 flex items-center">
            <router-link to="/board/3" class="text-dark-500 font-bold hover:underline mr-2">알바생 게시판</router-link>
          </li>
        </ul>
      </div>
    </section>
  </div>
    <div class="max-w-4xl mx-auto">
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
  </style>
  