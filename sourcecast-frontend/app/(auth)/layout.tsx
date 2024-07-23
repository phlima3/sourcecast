import { Logo } from "./_components/logo";

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="h-full flex items-center justify-center flex-col gap-4">
      <Logo />
      {children}
    </div>
  );
}
