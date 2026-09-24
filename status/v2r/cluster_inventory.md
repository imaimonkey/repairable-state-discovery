# V2R cluster inventory

2026-09-24T15:47:55.167828+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026011648 available bytes; 81.92% used; 112481450 free inodes.

server1 `/home`: 324026011648 available bytes; 81.92% used; 112481450 free inodes.

server1 `/tmp`: 324026011648 available bytes; 81.92% used; 112481450 free inodes.

server1 `/var/tmp`: 324026011648 available bytes; 81.92% used; 112481450 free inodes.

server1 `/mnt/raid5`: 416706908160 available bytes; 98.09% used; 337659097 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57369698304 available bytes; 96.80% used; 110427322 free inodes.

server2 `/home`: 57369698304 available bytes; 96.80% used; 110427322 free inodes.

server2 `/tmp`: 57369698304 available bytes; 96.80% used; 110427322 free inodes.

server2 `/var/tmp`: 57369698304 available bytes; 96.80% used; 110427322 free inodes.

server2 `/mnt/raid5`: 502244098048 available bytes; 96.53% used; 445165429 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84641353728 available bytes; 95.28% used; 114173314 free inodes.

server3 `/home`: 84641353728 available bytes; 95.28% used; 114173314 free inodes.

server3 `/data`: 160168243200 available bytes; 97.79% used; 225806199 free inodes.

server3 `/tmp`: 84641353728 available bytes; 95.28% used; 114173314 free inodes.

server3 `/var/tmp`: 84641353728 available bytes; 95.28% used; 114173314 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105707167744 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105707167744 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89363279872 available bytes; 98.76% used; 225256577 free inodes.

server4 `/tmp`: 105707167744 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105707167744 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
