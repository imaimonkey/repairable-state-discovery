# V2R cluster inventory

2026-09-24T01:03:25.333097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325524860928 available bytes; 81.84% used; 112500239 free inodes.

server1 `/home`: 325524860928 available bytes; 81.84% used; 112500239 free inodes.

server1 `/tmp`: 325524860928 available bytes; 81.84% used; 112500239 free inodes.

server1 `/var/tmp`: 325524860928 available bytes; 81.84% used; 112500239 free inodes.

server1 `/mnt/raid5`: 1004545589248 available bytes; 95.39% used; 337734877 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40969342976 available bytes; 97.71% used; 110432200 free inodes.

server2 `/home`: 40969342976 available bytes; 97.71% used; 110432200 free inodes.

server2 `/tmp`: 40969342976 available bytes; 97.71% used; 110432200 free inodes.

server2 `/var/tmp`: 40969342976 available bytes; 97.71% used; 110432200 free inodes.

server2 `/mnt/raid5`: 531748700160 available bytes; 96.33% used; 445202292 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292426399744 available bytes; 83.68% used; 114197498 free inodes.

server3 `/home`: 292426399744 available bytes; 83.68% used; 114197498 free inodes.

server3 `/data`: 82086105088 available bytes; 98.87% used; 225843217 free inodes.

server3 `/tmp`: 292426399744 available bytes; 83.68% used; 114197498 free inodes.

server3 `/var/tmp`: 292426399744 available bytes; 83.68% used; 114197498 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106014810112 available bytes; 94.08% used; 114349457 free inodes.

server4 `/home`: 106014810112 available bytes; 94.08% used; 114349457 free inodes.

server4 `/data`: 292723056640 available bytes; 95.95% used; 225405427 free inodes.

server4 `/tmp`: 106014810112 available bytes; 94.08% used; 114349457 free inodes.

server4 `/var/tmp`: 106014810112 available bytes; 94.08% used; 114349457 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
