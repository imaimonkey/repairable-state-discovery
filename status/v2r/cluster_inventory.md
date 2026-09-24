# V2R cluster inventory

2026-09-24T15:43:15.386917+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324018798592 available bytes; 81.92% used; 112481447 free inodes.

server1 `/home`: 324018798592 available bytes; 81.92% used; 112481447 free inodes.

server1 `/tmp`: 324018798592 available bytes; 81.92% used; 112481447 free inodes.

server1 `/var/tmp`: 324018798592 available bytes; 81.92% used; 112481447 free inodes.

server1 `/mnt/raid5`: 416718979072 available bytes; 98.09% used; 337659639 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57375236096 available bytes; 96.80% used; 110427373 free inodes.

server2 `/home`: 57375236096 available bytes; 96.80% used; 110427373 free inodes.

server2 `/tmp`: 57375236096 available bytes; 96.80% used; 110427373 free inodes.

server2 `/var/tmp`: 57375236096 available bytes; 96.80% used; 110427373 free inodes.

server2 `/mnt/raid5`: 502390685696 available bytes; 96.53% used; 445165727 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84855373824 available bytes; 95.26% used; 114182316 free inodes.

server3 `/home`: 84855373824 available bytes; 95.26% used; 114182316 free inodes.

server3 `/data`: 160203173888 available bytes; 97.79% used; 225806283 free inodes.

server3 `/tmp`: 84855373824 available bytes; 95.26% used; 114182316 free inodes.

server3 `/var/tmp`: 84855373824 available bytes; 95.26% used; 114182316 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105715736576 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105715736576 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89378156544 available bytes; 98.76% used; 225256594 free inodes.

server4 `/tmp`: 105715736576 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105715736576 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
