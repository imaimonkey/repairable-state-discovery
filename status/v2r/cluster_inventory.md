# V2R cluster inventory

2026-09-24T15:18:32.823274+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324039696384 available bytes; 81.92% used; 112481439 free inodes.

server1 `/home`: 324039696384 available bytes; 81.92% used; 112481439 free inodes.

server1 `/tmp`: 324039696384 available bytes; 81.92% used; 112481439 free inodes.

server1 `/var/tmp`: 324039696384 available bytes; 81.92% used; 112481439 free inodes.

server1 `/mnt/raid5`: 416790147072 available bytes; 98.09% used; 337662558 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57405259776 available bytes; 96.80% used; 110427623 free inodes.

server2 `/home`: 57405259776 available bytes; 96.80% used; 110427623 free inodes.

server2 `/tmp`: 57405259776 available bytes; 96.80% used; 110427623 free inodes.

server2 `/var/tmp`: 57405259776 available bytes; 96.80% used; 110427623 free inodes.

server2 `/mnt/raid5`: 503092203520 available bytes; 96.52% used; 445166499 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84476448768 available bytes; 95.29% used; 114158478 free inodes.

server3 `/home`: 84476448768 available bytes; 95.29% used; 114158478 free inodes.

server3 `/data`: 160457334784 available bytes; 97.78% used; 225807179 free inodes.

server3 `/tmp`: 84476448768 available bytes; 95.29% used; 114158478 free inodes.

server3 `/var/tmp`: 84476448768 available bytes; 95.29% used; 114158478 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716723712 available bytes; 94.10% used; 114348626 free inodes.

server4 `/home`: 105716723712 available bytes; 94.10% used; 114348626 free inodes.

server4 `/data`: 89424711680 available bytes; 98.76% used; 225256949 free inodes.

server4 `/tmp`: 105716723712 available bytes; 94.10% used; 114348626 free inodes.

server4 `/var/tmp`: 105716723712 available bytes; 94.10% used; 114348626 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
