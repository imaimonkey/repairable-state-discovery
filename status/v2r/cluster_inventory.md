# V2R cluster inventory

2026-09-24T15:21:38.646706+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324028571648 available bytes; 81.92% used; 112481440 free inodes.

server1 `/home`: 324028571648 available bytes; 81.92% used; 112481440 free inodes.

server1 `/tmp`: 324028571648 available bytes; 81.92% used; 112481440 free inodes.

server1 `/var/tmp`: 324028571648 available bytes; 81.92% used; 112481440 free inodes.

server1 `/mnt/raid5`: 416776028160 available bytes; 98.09% used; 337662174 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57403494400 available bytes; 96.80% used; 110427589 free inodes.

server2 `/home`: 57403494400 available bytes; 96.80% used; 110427589 free inodes.

server2 `/tmp`: 57403494400 available bytes; 96.80% used; 110427589 free inodes.

server2 `/var/tmp`: 57403494400 available bytes; 96.80% used; 110427589 free inodes.

server2 `/mnt/raid5`: 503004528640 available bytes; 96.52% used; 445166392 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84871983104 available bytes; 95.26% used; 114184583 free inodes.

server3 `/home`: 84871983104 available bytes; 95.26% used; 114184583 free inodes.

server3 `/data`: 160440426496 available bytes; 97.78% used; 225807124 free inodes.

server3 `/tmp`: 84871983104 available bytes; 95.26% used; 114184583 free inodes.

server3 `/var/tmp`: 84871983104 available bytes; 95.26% used; 114184583 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716576256 available bytes; 94.10% used; 114348626 free inodes.

server4 `/home`: 105716576256 available bytes; 94.10% used; 114348626 free inodes.

server4 `/data`: 89423265792 available bytes; 98.76% used; 225256945 free inodes.

server4 `/tmp`: 105716576256 available bytes; 94.10% used; 114348626 free inodes.

server4 `/var/tmp`: 105716576256 available bytes; 94.10% used; 114348626 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
