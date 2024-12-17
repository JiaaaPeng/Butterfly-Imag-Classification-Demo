module.exports = {
    root: true,
    env: {
        node: true
    },
    extends: [
        'plugin:vue/vue3-essential',
        'eslint:recommended'
    ],
    parserOptions: {
        parser: '@babel/eslint-parser'
    },
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        // 禁用组件名必须多个单词的规则
        'vue/multi-word-component-names': 'off',
        // 如果还有其他烦人的规则，可以在这里禁用
        'vue/no-multiple-template-root': 'off'
    }
} 