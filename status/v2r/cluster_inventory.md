# V2R cluster inventory

2026-09-24T06:37:47.106231+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324501336064 available bytes; 81.90% used; 112491598 free inodes.

server1 `/home`: 324501336064 available bytes; 81.90% used; 112491598 free inodes.

server1 `/tmp`: 324501336064 available bytes; 81.90% used; 112491598 free inodes.

server1 `/var/tmp`: 324501336064 available bytes; 81.90% used; 112491598 free inodes.

server1 `/mnt/raid5`: 517576519680 available bytes; 97.63% used; 337723745 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57876054016 available bytes; 96.77% used; 110431203 free inodes.

server2 `/home`: 57876054016 available bytes; 96.77% used; 110431203 free inodes.

server2 `/tmp`: 57876054016 available bytes; 96.77% used; 110431203 free inodes.

server2 `/var/tmp`: 57876054016 available bytes; 96.77% used; 110431203 free inodes.

server2 `/mnt/raid5`: 520023015424 available bytes; 96.41% used; 445192069 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126914580480 available bytes; 92.92% used; 114195218 free inodes.

server3 `/home`: 126914580480 available bytes; 92.92% used; 114195218 free inodes.

server3 `/data`: 139412725760 available bytes; 98.07% used; 225835603 free inodes.

server3 `/tmp`: 126914580480 available bytes; 92.92% used; 114195218 free inodes.

server3 `/var/tmp`: 126914580480 available bytes; 92.92% used; 114195218 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105805090816 available bytes; 94.10% used; 114349256 free inodes.

server4 `/home`: 105805090816 available bytes; 94.10% used; 114349256 free inodes.

server4 `/data`: 321921724416 available bytes; 95.55% used; 225372448 free inodes.

server4 `/tmp`: 105805090816 available bytes; 94.10% used; 114349256 free inodes.

server4 `/var/tmp`: 105805090816 available bytes; 94.10% used; 114349256 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
