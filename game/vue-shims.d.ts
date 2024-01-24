declare module '*.vue' {
    import type { DefineComponent } from 'vue'
    const component: DefineComponent<{}, {}, any>
    export default component
}

interface ImportMetaEnv {
    // Повторите каждую переменную окружения, которую вы ожидаете использовать
    readonly BASE_URL: string;
    // ... другие переменные окружения
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}