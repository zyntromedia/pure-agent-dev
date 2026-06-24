Set up Vercel Connect and initialize it with the following example:

1. Install the skill:

```bash
npx skills add vercel/vercel-plugin --skill vercel-connect
```

2. Connect a service:

```bash
vercel connect create github --name acme-github
```

3. Read its data:

```ts
import { getToken } from '@vercel/connect';

const token = await getToken('github/acme-github');
```