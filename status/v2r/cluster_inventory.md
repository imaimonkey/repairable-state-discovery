# V2R cluster inventory

2026-09-25T08:05:57.726641+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318845153280 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318845153280 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318845153280 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318845153280 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 386586439680 available bytes; 98.23% used; 337557853 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22843494400 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22843494400 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22843494400 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22843494400 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 334022615040 available bytes; 97.69% used; 445095214 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436627456 available bytes; 95.29% used; 114156053 free inodes.

server3 `/home`: 84436627456 available bytes; 95.29% used; 114156053 free inodes.

server3 `/data`: 142391259136 available bytes; 98.03% used; 225812103 free inodes.

server3 `/tmp`: 84436627456 available bytes; 95.29% used; 114156053 free inodes.

server3 `/var/tmp`: 84436627456 available bytes; 95.29% used; 114156053 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105625366528 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625366528 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249027858432 available bytes; 96.56% used; 225008967 free inodes.

server4 `/tmp`: 105625366528 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625366528 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
