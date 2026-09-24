# V2R cluster inventory

2026-09-24T16:22:23.551930+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024041472 available bytes; 81.92% used; 112481446 free inodes.

server1 `/home`: 324024041472 available bytes; 81.92% used; 112481446 free inodes.

server1 `/tmp`: 324024041472 available bytes; 81.92% used; 112481446 free inodes.

server1 `/var/tmp`: 324024041472 available bytes; 81.92% used; 112481446 free inodes.

server1 `/mnt/raid5`: 416583180288 available bytes; 98.09% used; 337654280 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57331916800 available bytes; 96.80% used; 110426963 free inodes.

server2 `/home`: 57331916800 available bytes; 96.80% used; 110426963 free inodes.

server2 `/tmp`: 57331916800 available bytes; 96.80% used; 110426963 free inodes.

server2 `/var/tmp`: 57331916800 available bytes; 96.80% used; 110426963 free inodes.

server2 `/mnt/raid5`: 501194194944 available bytes; 96.54% used; 445164803 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84330115072 available bytes; 95.29% used; 114154489 free inodes.

server3 `/home`: 84330115072 available bytes; 95.29% used; 114154489 free inodes.

server3 `/data`: 159564066816 available bytes; 97.79% used; 225788191 free inodes.

server3 `/tmp`: 84330115072 available bytes; 95.29% used; 114154489 free inodes.

server3 `/var/tmp`: 84330115072 available bytes; 95.29% used; 114154489 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697337344 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697337344 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89288581120 available bytes; 98.77% used; 225255960 free inodes.

server4 `/tmp`: 105697337344 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697337344 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
