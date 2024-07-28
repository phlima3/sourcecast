"use client";

import { Button } from "@/components/ui/button";
import { useSidebar } from "@/store/use-sidebar";
import { ArrowLeftFromLine, ArrowRightFromLine } from "lucide-react";
import { Hint } from "@/components/hint";
export const Toggle = () => {
  const { collapsed, onCollapse, onExpand } = useSidebar();

  const label = collapsed ? "Expand" : "Collapse";

  return (
    <>
      {collapsed ? (
        <div className="hidden lg:flex w-full items-center justify-center pt-4 mb-4">
          <Hint label={label} side="right" align="end" asChild>
            <Button className="h-auto p-2" variant="ghost" onClick={onExpand}>
              <ArrowRightFromLine className="w-4 h-4" />
            </Button>
          </Hint>
        </div>
      ) : (
        <div className="p-3 pl-6 mb-2 flex items-center w-full transition-all ease-in-out">
          <p className="font-semibold text-primary">For you</p>

          <Hint label={label} side="right" asChild>
            <Button
              onClick={onCollapse}
              className="h-auto p-2 ml-auto"
              variant="ghost"
            >
              <ArrowLeftFromLine className="w-4 h-4" />
            </Button>
          </Hint>
        </div>
      )}
    </>
  );
};
