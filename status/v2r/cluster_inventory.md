# V2R cluster inventory

2026-09-24T16:13:07.011317+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026511360 available bytes; 81.92% used; 112481455 free inodes.

server1 `/home`: 324026511360 available bytes; 81.92% used; 112481455 free inodes.

server1 `/tmp`: 324026511360 available bytes; 81.92% used; 112481455 free inodes.

server1 `/var/tmp`: 324026511360 available bytes; 81.92% used; 112481455 free inodes.

server1 `/mnt/raid5`: 416610050048 available bytes; 98.09% used; 337655357 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57346097152 available bytes; 96.80% used; 110427071 free inodes.

server2 `/home`: 57346097152 available bytes; 96.80% used; 110427071 free inodes.

server2 `/tmp`: 57346097152 available bytes; 96.80% used; 110427071 free inodes.

server2 `/var/tmp`: 57346097152 available bytes; 96.80% used; 110427071 free inodes.

server2 `/mnt/raid5`: 501488099328 available bytes; 96.53% used; 445165339 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84323561472 available bytes; 95.29% used; 114153901 free inodes.

server3 `/home`: 84323561472 available bytes; 95.29% used; 114153901 free inodes.

server3 `/data`: 159999815680 available bytes; 97.79% used; 225805623 free inodes.

server3 `/tmp`: 84323561472 available bytes; 95.29% used; 114153901 free inodes.

server3 `/var/tmp`: 84323561472 available bytes; 95.29% used; 114153901 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697726464 available bytes; 94.10% used; 114348606 free inodes.

server4 `/home`: 105697726464 available bytes; 94.10% used; 114348606 free inodes.

server4 `/data`: 89321148416 available bytes; 98.77% used; 225256123 free inodes.

server4 `/tmp`: 105697726464 available bytes; 94.10% used; 114348606 free inodes.

server4 `/var/tmp`: 105697726464 available bytes; 94.10% used; 114348606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
