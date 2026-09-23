# V2R cluster inventory

2026-09-23T16:58:21.283532+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41394122752 available bytes; 97.69% used; 110435441 free inodes.

server2 `/home`: 41394122752 available bytes; 97.69% used; 110435441 free inodes.

server2 `/tmp`: 41394122752 available bytes; 97.69% used; 110435441 free inodes.

server2 `/var/tmp`: 41394122752 available bytes; 97.69% used; 110435441 free inodes.

server2 `/mnt/raid5`: 547788648448 available bytes; 96.21% used; 445216951 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 294685016064 available bytes; 83.56% used; 114284941 free inodes.

server3 `/home`: 294685016064 available bytes; 83.56% used; 114284941 free inodes.

server3 `/data`: 53155143680 available bytes; 99.27% used; 225853072 free inodes.

server3 `/tmp`: 294685016064 available bytes; 83.56% used; 114284941 free inodes.

server3 `/var/tmp`: 294685016064 available bytes; 83.56% used; 114284941 free inodes.
| server4 | True | ['1', '2', '3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111489708032 available bytes; 93.78% used; 114375793 free inodes.

server4 `/home`: 111489708032 available bytes; 93.78% used; 114375793 free inodes.

server4 `/data`: 32936415232 available bytes; 99.54% used; 225477770 free inodes.

server4 `/tmp`: 111489708032 available bytes; 93.78% used; 114375793 free inodes.

server4 `/var/tmp`: 111489708032 available bytes; 93.78% used; 114375793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
