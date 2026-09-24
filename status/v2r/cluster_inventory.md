# V2R cluster inventory

2026-09-24T01:28:13.763229+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325463076864 available bytes; 81.84% used; 112499688 free inodes.

server1 `/home`: 325463076864 available bytes; 81.84% used; 112499688 free inodes.

server1 `/tmp`: 325463076864 available bytes; 81.84% used; 112499688 free inodes.

server1 `/var/tmp`: 325463076864 available bytes; 81.84% used; 112499688 free inodes.

server1 `/mnt/raid5`: 905847705600 available bytes; 95.84% used; 337734016 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40950013952 available bytes; 97.72% used; 110432011 free inodes.

server2 `/home`: 40950013952 available bytes; 97.72% used; 110432011 free inodes.

server2 `/tmp`: 40950013952 available bytes; 97.72% used; 110432011 free inodes.

server2 `/var/tmp`: 40950013952 available bytes; 97.72% used; 110432011 free inodes.

server2 `/mnt/raid5`: 530475397120 available bytes; 96.33% used; 445201558 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.

server3 `/home`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.

server3 `/data`: 82042351616 available bytes; 98.87% used; 225842307 free inodes.

server3 `/tmp`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.

server3 `/var/tmp`: 292699897856 available bytes; 83.67% used; 114210371 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105969418240 available bytes; 94.09% used; 114348864 free inodes.

server4 `/home`: 105969418240 available bytes; 94.09% used; 114348864 free inodes.

server4 `/data`: 290810249216 available bytes; 95.98% used; 225396968 free inodes.

server4 `/tmp`: 105969418240 available bytes; 94.09% used; 114348864 free inodes.

server4 `/var/tmp`: 105969418240 available bytes; 94.09% used; 114348864 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
