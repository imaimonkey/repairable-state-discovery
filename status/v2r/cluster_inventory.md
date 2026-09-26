# V2R cluster inventory

2026-09-26T07:30:36.578203+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318768295936 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318768295936 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318768295936 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318768295936 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 219234480128 available bytes; 98.99% used; 337539235 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22321750016 available bytes; 98.75% used; 110403925 free inodes.

server2 `/home`: 22321750016 available bytes; 98.75% used; 110403925 free inodes.

server2 `/tmp`: 22321750016 available bytes; 98.75% used; 110403925 free inodes.

server2 `/var/tmp`: 22321750016 available bytes; 98.75% used; 110403925 free inodes.

server2 `/mnt/raid5`: 271454752768 available bytes; 98.12% used; 445026853 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679566336 available bytes; 95.39% used; 114110897 free inodes.

server3 `/home`: 82679566336 available bytes; 95.39% used; 114110897 free inodes.

server3 `/data`: 123977297920 available bytes; 98.29% used; 225821078 free inodes.

server3 `/tmp`: 82679566336 available bytes; 95.39% used; 114110897 free inodes.

server3 `/var/tmp`: 82679566336 available bytes; 95.39% used; 114110897 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106074472448 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106074472448 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105863282688 available bytes; 98.54% used; 224922704 free inodes.

server4 `/tmp`: 106074472448 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106074472448 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
