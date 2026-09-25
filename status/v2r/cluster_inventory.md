# V2R cluster inventory

2026-09-25T18:58:37.157684+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318739189760 available bytes; 82.22% used; 112476329 free inodes.

server1 `/home`: 318739189760 available bytes; 82.22% used; 112476329 free inodes.

server1 `/tmp`: 318739189760 available bytes; 82.22% used; 112476329 free inodes.

server1 `/var/tmp`: 318739189760 available bytes; 82.22% used; 112476329 free inodes.

server1 `/mnt/raid5`: 371030466560 available bytes; 98.30% used; 337540981 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23097827328 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23097827328 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23097827328 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23097827328 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 312994529280 available bytes; 97.84% used; 445065541 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382941184 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382941184 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131369349120 available bytes; 98.18% used; 225809125 free inodes.

server3 `/tmp`: 84382941184 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382941184 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105606606848 available bytes; 94.11% used; 114349595 free inodes.

server4 `/home`: 105606606848 available bytes; 94.11% used; 114349595 free inodes.

server4 `/data`: 229681881088 available bytes; 96.83% used; 224931336 free inodes.

server4 `/tmp`: 105606606848 available bytes; 94.11% used; 114349595 free inodes.

server4 `/var/tmp`: 105606606848 available bytes; 94.11% used; 114349595 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
