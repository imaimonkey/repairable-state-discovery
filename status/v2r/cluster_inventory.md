# V2R cluster inventory

2026-09-24T16:19:18.203652+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024668160 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324024668160 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324024668160 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324024668160 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 395941478400 available bytes; 98.18% used; 337654635 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57334378496 available bytes; 96.80% used; 110426995 free inodes.

server2 `/home`: 57334378496 available bytes; 96.80% used; 110426995 free inodes.

server2 `/tmp`: 57334378496 available bytes; 96.80% used; 110426995 free inodes.

server2 `/var/tmp`: 57334378496 available bytes; 96.80% used; 110426995 free inodes.

server2 `/mnt/raid5`: 501291171840 available bytes; 96.54% used; 445164884 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84716081152 available bytes; 95.27% used; 114180094 free inodes.

server3 `/home`: 84716081152 available bytes; 95.27% used; 114180094 free inodes.

server3 `/data`: 159613317120 available bytes; 97.79% used; 225789323 free inodes.

server3 `/tmp`: 84716081152 available bytes; 95.27% used; 114180094 free inodes.

server3 `/var/tmp`: 84716081152 available bytes; 95.27% used; 114180094 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105697456128 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697456128 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89291296768 available bytes; 98.77% used; 225255966 free inodes.

server4 `/tmp`: 105697456128 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697456128 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
