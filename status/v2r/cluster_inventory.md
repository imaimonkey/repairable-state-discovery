# V2R cluster inventory

2026-09-25T21:37:16.538314+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318701527040 available bytes; 82.22% used; 112476316 free inodes.

server1 `/home`: 318701527040 available bytes; 82.22% used; 112476316 free inodes.

server1 `/tmp`: 318701527040 available bytes; 82.22% used; 112476316 free inodes.

server1 `/var/tmp`: 318701527040 available bytes; 82.22% used; 112476316 free inodes.

server1 `/mnt/raid5`: 360510414848 available bytes; 98.35% used; 337539241 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22900322304 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22900322304 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22900322304 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22900322304 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 301044981760 available bytes; 97.92% used; 445054521 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84367323136 available bytes; 95.29% used; 114152626 free inodes.

server3 `/home`: 84367323136 available bytes; 95.29% used; 114152626 free inodes.

server3 `/data`: 125891076096 available bytes; 98.26% used; 225806864 free inodes.

server3 `/tmp`: 84367323136 available bytes; 95.29% used; 114152626 free inodes.

server3 `/var/tmp`: 84367323136 available bytes; 95.29% used; 114152626 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105388814336 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105388814336 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 216841142272 available bytes; 97.00% used; 224919916 free inodes.

server4 `/tmp`: 105388814336 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105388814336 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
