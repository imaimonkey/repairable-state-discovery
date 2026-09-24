# V2R cluster inventory

2026-09-24T16:16:12.645479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025257984 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324025257984 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324025257984 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324025257984 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416601010176 available bytes; 98.09% used; 337654994 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57342947328 available bytes; 96.80% used; 110427029 free inodes.

server2 `/home`: 57342947328 available bytes; 96.80% used; 110427029 free inodes.

server2 `/tmp`: 57342947328 available bytes; 96.80% used; 110427029 free inodes.

server2 `/var/tmp`: 57342947328 available bytes; 96.80% used; 110427029 free inodes.

server2 `/mnt/raid5`: 501378789376 available bytes; 96.54% used; 445165006 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84395786240 available bytes; 95.29% used; 114164532 free inodes.

server3 `/home`: 84395786240 available bytes; 95.29% used; 114164532 free inodes.

server3 `/data`: 159976464384 available bytes; 97.79% used; 225805508 free inodes.

server3 `/tmp`: 84395786240 available bytes; 95.29% used; 114164532 free inodes.

server3 `/var/tmp`: 84395786240 available bytes; 95.29% used; 114164532 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697566720 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697566720 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89300561920 available bytes; 98.77% used; 225256021 free inodes.

server4 `/tmp`: 105697566720 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697566720 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
