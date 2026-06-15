# React Flow Reference

공식 문서 보조 레퍼런스. 구현 전 [SKILL.md](SKILL.md) 워크플로우를 먼저 따른다.

## Node 옵션 (자주 쓰는 것)

| Prop | 타입 | 설명 |
|------|------|------|
| `id` | string | 고유 ID |
| `type` | string | `nodeTypes` 키 |
| `position` | `{ x, y }` | viewport 좌표 (parent 있으면 상대) |
| `data` | object | 커스텀 payload |
| `parentId` | string | 부모 노드 ID (sub-flow) |
| `extent` | `'parent'` \| CoordinateExtent | 이동 경계 |
| `expandParent` | boolean | 부모 자동 확장 |
| `draggable` | boolean | 드래그 가능 여부 |
| `selectable` | boolean | 선택 가능 여부 |
| `connectable` | boolean | 연결 가능 여부 |
| `hidden` | boolean | 숨김 |
| `style` | CSSProperties | 인라인 스타일 (그룹 크기 등) |
| `zIndex` | number | 선택 시 자동 상승 |

## Edge 옵션 (자주 쓰는 것)

| Prop | 타입 | 설명 |
|------|------|------|
| `id` | string | 고유 ID |
| `source` / `target` | string | 노드 ID |
| `sourceHandle` / `targetHandle` | string | 특정 핸들 ID |
| `type` | string | `edgeTypes` 키 |
| `label` | ReactNode | 엣지 라벨 |
| `animated` | boolean | 애니메이션 |
| `hidden` | boolean | 숨김 |

## ReactFlow 주요 Props

### 데이터·이벤트

- `nodes`, `edges` — controlled state
- `defaultNodes`, `defaultEdges` — uncontrolled 초기값
- `onNodesChange`, `onEdgesChange`, `onConnect`
- `onSelectionChange`, `onNodeDrag`, `onNodeClick`, `onEdgeClick`

### 타입 등록

- `nodeTypes`, `edgeTypes` — 컴포넌트 외부 상수

### 뷰포트·상호작용

- `fitView`, `fitViewOptions` (`padding` 등)
- `defaultEdgeOptions` — 모든 엣지 기본값
- `panOnDrag`, `panOnScroll`, `zoomOnScroll`, `zoomOnPinch`
- `selectionOnDrag`, `selectionMode` (`full` | `partial`)
- `nodesDraggable`, `nodesConnectable`, `elementsSelectable`
- `connectionMode` — `Strict` | `Loose`
- `deleteKeyCode`, `selectionKeyCode`, `multiSelectionKeyCode`

### 접근성

- `nodesFocusable`, `edgesFocusable`, `disableKeyboardA11y`
- `autoPanOnNodeFocus`, `ariaLabelConfig`
- 노드 `ariaRole`, `domAttributes`

## Hooks

| Hook | 용도 |
|------|------|
| `useReactFlow` | `getNodes`, `setNodes`, `fitView`, `screenToFlowPosition` 등 |
| `useNodesState` / `useEdgesState` | 로컬 state + change handler 래퍼 |
| `useStore` | 내부 store selector (고급) |
| `useNodeConnections` | 노드 연결 조회 |
| `useNodesData` | 연결된 노드 data |
| `useUpdateNodeInternals` | 핸들 변경 후 내부 치수 갱신 |

`useReactFlow`는 `ReactFlowProvider` 하위에서만 동작.

```tsx
<ReactFlowProvider>
  <FlowEditor />
</ReactFlowProvider>
```

## 경로(Path) 유틸

| 함수 | 설명 |
|------|------|
| `getBezierPath` | 기본 곡선 |
| `getSmoothStepPath` | smoothstep 엣지 |
| `getStraightPath` | 직선 |
| `getSimpleBezierPath` | 단순 베지어 |

커스텀 SVG path: `M`(move), `L`(line), `Q`(quadratic) 등으로 `BaseEdge`에 `path` 전달.

## Change 이벤트 유틸

| 함수 | 설명 |
|------|------|
| `applyNodeChanges` | position, select, remove 등 노드 변경 반영 |
| `applyEdgeChanges` | 엣지 변경 반영 |
| `addEdge` | `onConnect` params로 새 엣지 추가 |

## 레이아웃 패턴 (dagre 예시)

```ts
import dagre from '@dagrejs/dagre';

function getLayoutedElements(nodes, edges, direction = 'TB') {
  const g = new dagre.graphlib.Graph().setDefaultEdgeLabel(() => ({}));
  g.setGraph({ rankdir: direction });

  nodes.forEach((node) => {
    g.setNode(node.id, { width: node.width ?? 150, height: node.height ?? 50 });
  });
  edges.forEach((edge) => g.setEdge(edge.source, edge.target));

  dagre.layout(g);

  return {
    nodes: nodes.map((node) => {
      const pos = g.node(node.id);
      return {
        ...node,
        position: {
          x: pos.x - (node.width ?? 150) / 2,
          y: pos.y - (node.height ?? 50) / 2,
        },
      };
    }),
    edges,
  };
}
```

노드 실제 크기(`measured.width/height`)를 dagre에 전달해야 정확함.

## React Flow UI 컴포넌트 카탈로그

설치: `npx shadcn@latest add https://ui.reactflow.dev/<slug>`

### Node Utilities

| Slug | 설명 |
|------|------|
| `base-node` | Header/Content/Footer 래퍼 |
| `node-status-indicator` | success/loading/error/initial 상태 |
| `node-appendix` | 노드 부가 정보·배지 |
| `node-tooltip` | 노드 툴팁 래퍼 |

### Custom Nodes (예시)

| Slug | 설명 |
|------|------|
| `database-schema-node` | DB 테이블·관계 시각화 |
| `annotation-node` | 주석 노드 (BaseNode 예시) |
| `labeled-group-node` | 라벨 그룹 |

### Handles

| Slug | 설명 |
|------|------|
| `base-handle` | 커스텀 핸들 베이스 |
| `button-handle` | 버튼형 핸들 |

### Custom Edges

| Slug | 설명 |
|------|------|
| `animated-svg-edge` | SVG 애니메이션 엣지 |
| `wire-edge` | 와이어 스타일 |

### Controls

| Slug | 설명 |
|------|------|
| `node-search` | Command 기반 노드 검색·fitView |
| `zoom-slider` | 줌 슬라이더 |

### Miscellaneous

| Slug | 설명 |
|------|------|
| `devtools` | 노드·플로우 상태 디버깅 |

전체 목록은 https://reactflow.dev/ui 에서 확인.

## React Flow UI + BaseNode 패턴

```tsx
import { memo } from 'react';
import { Button } from '@/components/ui/button';
import {
  BaseNode,
  BaseNodeContent,
  BaseNodeFooter,
  BaseNodeHeader,
  BaseNodeHeaderTitle,
} from '@/components/base-node';

export const MyNode = memo(({ data }: NodeProps<MyNodeType>) => (
  <BaseNode className="w-80">
    <BaseNodeHeader>
      <BaseNodeHeaderTitle>{data.label}</BaseNodeHeaderTitle>
    </BaseNodeHeader>
    <BaseNodeContent>{/* 본문 */}</BaseNodeContent>
    <BaseNodeFooter>
      <Button className="nodrag w-full" variant="outline">Action</Button>
    </BaseNodeFooter>
  </BaseNode>
));
MyNode.displayName = 'MyNode';
```

상태별 border: `cn()` + `data.status` 조건부 className.

## Node Search 패턴

```tsx
import { NodeSearch } from '@/components/node-search';
import { Panel, ReactFlow } from '@xyflow/react';

<ReactFlow ...>
  <Panel position="top-left">
    <NodeSearch />
  </Panel>
</ReactFlow>
```

- 기본: label lowercase 포함 검색 → 선택 + fitView
- `onSearch`, `onSelectNode`로 커스터마이즈

## MUI + React Flow 혼용 (Knock 등)

Tailwind/shadcn 없이 MUI만 쓰는 프로젝트는 React Flow UI 대신 **커스텀 노드 직접 구현**이 일반적.

- `@xyflow/react/dist/style.css` 별도 import
- 커스텀 Handle에 MUI Icon 래핑 가능 (Handle `style: { background: 'none', border: 'none' }`)
- 인터랙티브 MUI 컴포넌트에 `nodrag` className
- 그래프 로직(`flowGraph.ts` 등)과 UI 컴포넌트(`FlowCanvasNode`) 분리

## Pro Examples (참고)

- Parent-child 동적 attach/detach
- Editable edge
- Add node on edge drop

https://reactflow.dev/examples

## 공식 문서 링크

| 주제 | URL |
|------|-----|
| Quick Start | https://reactflow.dev/learn |
| Custom Nodes | https://reactflow.dev/learn/customization/custom-nodes |
| Handles | https://reactflow.dev/learn/customization/handles |
| Utility Classes | https://reactflow.dev/learn/customization/utility-classes |
| Custom Edges | https://reactflow.dev/learn/customization/custom-edges |
| TypeScript | https://reactflow.dev/learn/advanced-use/typescript |
| State Management | https://reactflow.dev/learn/advanced-use/state-management |
| Layouting | https://reactflow.dev/learn/layouting/layouting |
| Sub-flows | https://reactflow.dev/learn/layouting/sub-flows |
| Viewport | https://reactflow.dev/learn/concepts/the-viewport |
| Accessibility | https://reactflow.dev/learn/advanced-use/accessibility |
| React Flow UI | https://reactflow.dev/ui |
