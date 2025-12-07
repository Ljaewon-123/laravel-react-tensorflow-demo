import { TextareaWithButton } from "@/components/textarea-with-button"
import { useEffect, useState } from "react"
import { toast } from "sonner"

const requestMessage = async( message: string) => {
  const res = await fetch('/api/sentiment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message }),
  });

  const data = await res.json();
  return data;
}

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
      const res = await requestMessage(message)

      if (!res.ok) throw new Error("API Error")

      const data = await res.json()
      setResult(JSON.stringify(data, null, 2))

      toast.success("감정 분석 성공!")
    } catch (err) {
      toast.error("분석에 실패했습니다.")
    }
  }

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
