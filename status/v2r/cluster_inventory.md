# V2R cluster inventory

2026-09-23T21:08:54.990429+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325718913024 available bytes; 81.83% used; 112501443 free inodes.

server1 `/home`: 325718913024 available bytes; 81.83% used; 112501443 free inodes.

server1 `/tmp`: 325718913024 available bytes; 81.83% used; 112501443 free inodes.

server1 `/var/tmp`: 325718913024 available bytes; 81.83% used; 112501443 free inodes.

server1 `/mnt/raid5`: 1388137529344 available bytes; 93.63% used; 337739986 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41120456704 available bytes; 97.71% used; 110432708 free inodes.

server2 `/home`: 41120456704 available bytes; 97.71% used; 110432708 free inodes.

server2 `/tmp`: 41120456704 available bytes; 97.71% used; 110432708 free inodes.

server2 `/var/tmp`: 41120456704 available bytes; 97.71% used; 110432708 free inodes.

server2 `/mnt/raid5`: 539170209792 available bytes; 96.27% used; 445209422 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293463248896 available bytes; 83.62% used; 114237001 free inodes.

server3 `/home`: 293463248896 available bytes; 83.62% used; 114237001 free inodes.

server3 `/data`: 52315299840 available bytes; 99.28% used; 225849552 free inodes.

server3 `/tmp`: 293463248896 available bytes; 83.62% used; 114237001 free inodes.

server3 `/var/tmp`: 293463248896 available bytes; 83.62% used; 114237001 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106494582784 available bytes; 94.06% used; 114356046 free inodes.

server4 `/home`: 106494582784 available bytes; 94.06% used; 114356046 free inodes.

server4 `/data`: 300500283392 available bytes; 95.85% used; 225455234 free inodes.

server4 `/tmp`: 106494582784 available bytes; 94.06% used; 114356046 free inodes.

server4 `/var/tmp`: 106494582784 available bytes; 94.06% used; 114356046 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
