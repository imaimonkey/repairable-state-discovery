# V2R cluster inventory

2026-09-26T15:08:46.698038+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318165233664 available bytes; 82.25% used; 112473929 free inodes.

server1 `/home`: 318165233664 available bytes; 82.25% used; 112473929 free inodes.

server1 `/tmp`: 318165233664 available bytes; 82.25% used; 112473929 free inodes.

server1 `/var/tmp`: 318165233664 available bytes; 82.25% used; 112473929 free inodes.

server1 `/mnt/raid5`: 654237728768 available bytes; 97.00% used; 337531845 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 40423424 available bytes; 100.00% used; 110366896 free inodes.

server2 `/home`: 40423424 available bytes; 100.00% used; 110366896 free inodes.

server2 `/tmp`: 40423424 available bytes; 100.00% used; 110366896 free inodes.

server2 `/var/tmp`: 40423424 available bytes; 100.00% used; 110366896 free inodes.

server2 `/mnt/raid5`: 613163585536 available bytes; 95.76% used; 444973100 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83163181056 available bytes; 95.36% used; 114139330 free inodes.

server3 `/home`: 83163181056 available bytes; 95.36% used; 114139330 free inodes.

server3 `/data`: 1346924040192 available bytes; 81.38% used; 225810557 free inodes.

server3 `/tmp`: 83163181056 available bytes; 95.36% used; 114139330 free inodes.

server3 `/var/tmp`: 83163181056 available bytes; 95.36% used; 114139330 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105955143680 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105955143680 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410814640128 available bytes; 94.32% used; 224826125 free inodes.

server4 `/tmp`: 105955143680 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105955143680 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
