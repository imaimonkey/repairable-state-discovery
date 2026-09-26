# V2R cluster inventory

2026-09-26T00:28:45.042625+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318653583360 available bytes; 82.22% used; 112476287 free inodes.

server1 `/home`: 318653583360 available bytes; 82.22% used; 112476287 free inodes.

server1 `/tmp`: 318653583360 available bytes; 82.22% used; 112476287 free inodes.

server1 `/var/tmp`: 318653583360 available bytes; 82.22% used; 112476287 free inodes.

server1 `/mnt/raid5`: 359397355520 available bytes; 98.35% used; 337546887 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941822976 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22941822976 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22941822976 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22941822976 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 295140118528 available bytes; 97.96% used; 445057761 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339712000 available bytes; 95.29% used; 114152443 free inodes.

server3 `/home`: 84339712000 available bytes; 95.29% used; 114152443 free inodes.

server3 `/data`: 124947247104 available bytes; 98.27% used; 225819083 free inodes.

server3 `/tmp`: 84339712000 available bytes; 95.29% used; 114152443 free inodes.

server3 `/var/tmp`: 84339712000 available bytes; 95.29% used; 114152443 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453223936 available bytes; 94.12% used; 114348365 free inodes.

server4 `/home`: 105453223936 available bytes; 94.12% used; 114348365 free inodes.

server4 `/data`: 177383645184 available bytes; 97.55% used; 224917509 free inodes.

server4 `/tmp`: 105453223936 available bytes; 94.12% used; 114348365 free inodes.

server4 `/var/tmp`: 105453223936 available bytes; 94.12% used; 114348365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
