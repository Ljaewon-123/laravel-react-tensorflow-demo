import { TextareaWithButton } from "@/components/textarea-with-button"
import { useEffect, useState } from "react"
import { toast } from "sonner"
import { Toaster } from "@/components/ui/sonner"

function getCookie(name: string) {
  return document.cookie
    .split('; ')
    .find(row => row.startsWith(name + '='))
    ?.split('=')[1];
}

const requestMessage = async (message: string) => {
  const token = getCookie('XSRF-TOKEN');

  const res = await fetch('/sentiment', {
    method: 'POST',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
      'X-XSRF-TOKEN': decodeURIComponent(token ?? ''),
    },
    body: JSON.stringify({ text: message }),
  });

  const data = await res.json();
  return data;
};


export default function MessagePage() {
  const [message, setMessage] = useState("")
  const [result, setResult] = useState<string>("")

  const handleSubmit = async () => {
    if (message.trim() === "") {
      toast("Incorrect Input Error", {
        description: "NOT Empty Message",
        action: {
          label: "Undo",
          onClick: () => console.log("Undo"),
        },
      })
      return
    }

    try {
      console.log('fetching!!!')
      const data = await requestMessage(message)
      setResult(JSON.stringify(data, null, 2))
      toast.success("감정 분석 성공!")
    } catch {
      console.log('왜 에러 로그가 없지')
      toast.error("분석에 실패했습니다.")
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center">
      <Toaster />
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
