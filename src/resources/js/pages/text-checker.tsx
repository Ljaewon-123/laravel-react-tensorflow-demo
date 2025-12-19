import { TextareaWithButton } from "@/components/textarea-with-button"
import { useEffect, useState } from "react"
import { toast } from "sonner"
import { router, usePage } from '@inertiajs/react';

export default function MessagePage() {
  const [message, setMessage] = useState("")
  const [result, setResult] = useState<string>("")

  const props = usePage().props

  const handleSubmit = () => {
    router.post('/sentiment', { 
      _token: props.csrf_token,
      message,
    });
  };


  return (
    <div className="min-h-screen flex flex-col items-center">
      <div className="mt-24 w-full max-w-md px-4">
        <TextareaWithButton
          value={message}
          onChange={setMessage}
          onSubmit={handleSubmit}
        />

        {/* message가 입력될 때마다 즉시 반영됨 */}
        {message && (
          <div className="mt-6 p-4 rounded-lg border bg-muted/30">
            <p className="font-semibold">입력한 내용:</p>
            <p className="text-sm text-muted-foreground">{message}</p>
          </div>
        )}
      </div>
    </div>
  )
}
