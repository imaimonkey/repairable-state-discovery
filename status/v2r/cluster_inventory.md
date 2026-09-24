# V2R cluster inventory

2026-09-24T03:20:52.538607+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325361397760 available bytes; 81.85% used; 112498250 free inodes.

server1 `/home`: 325361397760 available bytes; 81.85% used; 112498250 free inodes.

server1 `/tmp`: 325361397760 available bytes; 81.85% used; 112498250 free inodes.

server1 `/var/tmp`: 325361397760 available bytes; 81.85% used; 112498250 free inodes.

server1 `/mnt/raid5`: 435138039808 available bytes; 98.00% used; 337732373 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40846127104 available bytes; 97.72% used; 110431166 free inodes.

server2 `/home`: 40846127104 available bytes; 97.72% used; 110431166 free inodes.

server2 `/tmp`: 40846127104 available bytes; 97.72% used; 110431166 free inodes.

server2 `/var/tmp`: 40846127104 available bytes; 97.72% used; 110431166 free inodes.

server2 `/mnt/raid5`: 527430983680 available bytes; 96.36% used; 445197727 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292004700160 available bytes; 83.71% used; 114177763 free inodes.

server3 `/home`: 292004700160 available bytes; 83.71% used; 114177763 free inodes.

server3 `/data`: 39625957376 available bytes; 99.45% used; 225844076 free inodes.

server3 `/tmp`: 292004700160 available bytes; 83.71% used; 114177763 free inodes.

server3 `/var/tmp`: 292004700160 available bytes; 83.71% used; 114177763 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987448832 available bytes; 94.09% used; 114349611 free inodes.

server4 `/home`: 105987448832 available bytes; 94.09% used; 114349611 free inodes.

server4 `/data`: 288243474432 available bytes; 96.02% used; 225386444 free inodes.

server4 `/tmp`: 105987448832 available bytes; 94.09% used; 114349611 free inodes.

server4 `/var/tmp`: 105987448832 available bytes; 94.09% used; 114349611 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
