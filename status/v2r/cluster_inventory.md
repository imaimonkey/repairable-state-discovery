# V2R cluster inventory

2026-09-23T19:01:58.084274+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 331616710656 available bytes; 81.50% used; 112554804 free inodes.

server1 `/home`: 331616710656 available bytes; 81.50% used; 112554804 free inodes.

server1 `/tmp`: 331616710656 available bytes; 81.50% used; 112554804 free inodes.

server1 `/var/tmp`: 331616710656 available bytes; 81.50% used; 112554804 free inodes.

server1 `/mnt/raid5`: 1389249814528 available bytes; 93.63% used; 337741436 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41339883520 available bytes; 97.69% used; 110435448 free inodes.

server2 `/home`: 41339883520 available bytes; 97.69% used; 110435448 free inodes.

server2 `/tmp`: 41339883520 available bytes; 97.69% used; 110435448 free inodes.

server2 `/var/tmp`: 41339883520 available bytes; 97.69% used; 110435448 free inodes.

server2 `/mnt/raid5`: 543998382080 available bytes; 96.24% used; 445213628 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293544353792 available bytes; 83.62% used; 114238831 free inodes.

server3 `/home`: 293544353792 available bytes; 83.62% used; 114238831 free inodes.

server3 `/data`: 52785446912 available bytes; 99.27% used; 225846315 free inodes.

server3 `/tmp`: 293544353792 available bytes; 83.62% used; 114238831 free inodes.

server3 `/var/tmp`: 293544353792 available bytes; 83.62% used; 114238831 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106475704320 available bytes; 94.06% used; 114356234 free inodes.

server4 `/home`: 106475704320 available bytes; 94.06% used; 114356234 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 225457657 free inodes.

server4 `/tmp`: 106475704320 available bytes; 94.06% used; 114356234 free inodes.

server4 `/var/tmp`: 106475704320 available bytes; 94.06% used; 114356234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
