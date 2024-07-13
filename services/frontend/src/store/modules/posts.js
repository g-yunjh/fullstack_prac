import axios from 'axios';

const state = {
  posts: null,
  post: null
};

const getters = {
  statePosts: state => state.posts,
  statePost: state => state.post,
};

const actions = {
  async createPost({ dispatch }, post) {
    await axios.post('posts', post);
    await dispatch('getPosts');
  },
  async getPosts({ commit }) {
    let { data } = await axios.get('posts');
    commit('setPosts', data);
  },
  async viewPost({ commit }, id) {
    let { data } = await axios.get(`post/${id}`);
    commit('setPost', data);
  },
  async updatePost({ dispatch }, { id, form }) {
    await axios.patch(`post/${id}`, form);
    await dispatch('getPosts'); // 필요한 경우 게시물 목록 업데이트
  },
  async deletePost({ dispatch }, id) {
    await axios.delete(`post/${id}`);
    await dispatch('getPosts'); // 필요한 경우 게시물 목록 업데이트
  }
};

const mutations = {
  setPosts(state, posts) {
    state.posts = posts;
  },
  setPost(state, post) {
    state.post = post;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
