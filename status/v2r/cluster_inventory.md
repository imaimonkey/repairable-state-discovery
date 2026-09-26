# V2R cluster inventory

2026-09-26T07:33:39.966067+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318767640576 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318767640576 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318767640576 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318767640576 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219233972224 available bytes; 98.99% used; 337539237 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/home`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/tmp`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/var/tmp`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/mnt/raid5`: 271363817472 available bytes; 98.12% used; 445026777 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82681217024 available bytes; 95.39% used; 114110899 free inodes.

server3 `/home`: 82681217024 available bytes; 95.39% used; 114110899 free inodes.

server3 `/data`: 123976568832 available bytes; 98.29% used; 225821028 free inodes.

server3 `/tmp`: 82681217024 available bytes; 95.39% used; 114110899 free inodes.

server3 `/var/tmp`: 82681217024 available bytes; 95.39% used; 114110899 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106074390528 available bytes; 94.08% used; 114348173 free inodes.

server4 `/home`: 106074390528 available bytes; 94.08% used; 114348173 free inodes.

server4 `/data`: 105868021760 available bytes; 98.54% used; 224922705 free inodes.

server4 `/tmp`: 106074390528 available bytes; 94.08% used; 114348173 free inodes.

server4 `/var/tmp`: 106074390528 available bytes; 94.08% used; 114348173 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
