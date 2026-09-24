# V2R cluster inventory

2026-09-24T16:28:35.516755+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324023525376 available bytes; 81.92% used; 112481446 free inodes.

server1 `/home`: 324023525376 available bytes; 81.92% used; 112481446 free inodes.

server1 `/tmp`: 324023525376 available bytes; 81.92% used; 112481446 free inodes.

server1 `/var/tmp`: 324023525376 available bytes; 81.92% used; 112481446 free inodes.

server1 `/mnt/raid5`: 416573870080 available bytes; 98.09% used; 337653557 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57327656960 available bytes; 96.80% used; 110426898 free inodes.

server2 `/home`: 57327656960 available bytes; 96.80% used; 110426898 free inodes.

server2 `/tmp`: 57327656960 available bytes; 96.80% used; 110426898 free inodes.

server2 `/var/tmp`: 57327656960 available bytes; 96.80% used; 110426898 free inodes.

server2 `/mnt/raid5`: 500998807552 available bytes; 96.54% used; 445164407 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84704854016 available bytes; 95.27% used; 114179294 free inodes.

server3 `/home`: 84704854016 available bytes; 95.27% used; 114179294 free inodes.

server3 `/data`: 159367815168 available bytes; 97.80% used; 225788067 free inodes.

server3 `/tmp`: 84704854016 available bytes; 95.27% used; 114179294 free inodes.

server3 `/var/tmp`: 84704854016 available bytes; 95.27% used; 114179294 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697181696 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697181696 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89281437696 available bytes; 98.77% used; 225255848 free inodes.

server4 `/tmp`: 105697181696 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697181696 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
